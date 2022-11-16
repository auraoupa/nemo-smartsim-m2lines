"""
Example of a SmartSim driver that can be used to run a NEMO4-based
eORCA025 model. Currently, this only configures and runs a simulation.
Note a database is spun up, but it is not used by nemo4 at this time.
"""

from glob import glob
from smartsim import Experiment
from smartsim.database import Orchestrator
from smartsim.log import log_to_file
import warnings

def create_distributed_orchestrator(
    exp,
    orchestrator_port,
    orchestrator_interface,
    orchestrator_nodes,
    orchestrator_nemo_node_features,
    ):

    orchestrator = exp.create_database(
        port = orchestrator_port,
        interface = orchestrator_interface,
        db_nodes = orchestrator_nodes,
        threads_per_queue=2
    )

    if orchestrator_nemo_node_features:
        orchestrator.set_run_arg("constraint", orchestrator_nemo_node_features)
    return orchestrator

def create_nemo_model(
        experiment,
        nemo_num_nodes,
        nemo_tasks_per_node,
        nemo_node_features,
        xios_num_nodes,
        xios_tasks_per_node,
        xios_node_features,
        xios_exe,
        nemo_cfg_path,
        nemo_input_path,
        nemo_forcing_path
    ):

    # Create NEMO portion of the MPMD job
    nemo_run_settings = experiment.create_run_settings(
        f"{nemo_cfg_path}/BLD/bin/nemo.exe",
        run_command="srun"
    )

    # Add xios to the run settings and make it an MPMD model

    nemo_model = experiment.create_model(
        "nemo",
        run_settings   = nemo_run_settings,
    )
    xml_files = glob(f"{nemo_cfg_path}/EXPREF/*.xml")
    namelist_files = glob(f"{nemo_cfg_path}/EXP_SMSIM/namelist*")
    forcing_files = glob(f"{nemo_forcing_path}/*")
    forcing_files+= glob(f"{nemo_input_path}/*")

    nemo_model.attach_generator_files(
        to_configure=namelist_files,
        to_copy=xml_files,
        to_symlink=forcing_files
    )

    return nemo_model

def configure_nemo_model(
    model,
    job_number,
    first_time_step,
    last_time_step,
    restart_flag,
    restart_directory,
    ):

    nemo_config_options = {
        "NN_NO": job_number,
        "NIT000": first_time_step,
        "NITEND": last_time_step,
        "RESTART": restart_flag,
        "CN_DIRRST": restart_directory
    }

    model.params = nemo_config_options
    model.register_incoming_entity(model)

    return model

def nemo_clustered_driver(
    nemo_num_nodes=1,
    nemo_tasks_per_node=40,
    nemo_node_features=False,
    xios_num_nodes=1,
    xios_tasks_per_node=8,
    xios_node_features='',
    nemo_cfg_path="/gpfswork/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001",
    nemo_forcing_path="/gpfswork/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001/FORCING",
    nemo_input_path="/gpfswork/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001/MY_INPUTS",
    xios_exe="/gpfswork/rech/cli/rcst991/XIOS/bin/xios_server.exe",
    job_number = 1,
    first_time_step = 1,
    last_time_step = 6000,
    restart_flag = ".false.",
    restart_directory = "/gpfswork/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001",
    orchestrator_port=6780,
    orchestrator_interface='ib0',
    orchestrator_nodes=1,
    orchestrator_nemo_node_features=False
    ):
    """Run a nemo OM4_025 simulation with a cluster of databases used for
    machine-learning inference

    :param nemo_num_nodes: number of nodes allocated to nemo
    :type nemo_num_nodes: int, optional
    :param nemo_tasks_per_node: how many MPI ranks to be run per node
    :type nemo_tasks_per_node: int, optional
    :param nemo_node_features: features of the nodes that the nemo should run on
    :type nemo_node_features: int, optional
    :param nemo_cfg_path: full path to the nemo configuration directory
    :type nemo_cfg_path: str, optional
    :param nemo_forcing_path: full path to the nemo forcing directory
    :type nemo_forcing_path: str, optional
    :param xios_num_nodes: number of nodes allocated to XIOS
    :type xios_num_nodes: int, optional
    :param xios_tasks_per_node: how many MPI ranks to be run per node
    :type xios_tasks_per_node: int, optional
    :param xios_node_features: features of the nodes that the XIOS should run on
    :type xios_node_features: int, optional
    :param xios_exe: path to the XIOS executable
    :type xios_exe: str, optional
    :param nemo_cfg_path: full path to the nemo configuration directory
    :type nemo_cfg_path: str, optional
    :param nemo_forcing_path: full path to the nemo forcing directory
    :type nemo_forcing_path: str, optional
    :param job_number: The job number (nn_no) of the nemo experiment
    :type job_number: int, optional
    :param first_time_step: The first time step in the segment
    :type first_time_step: int, optional
    :param last_time_step: The last time step in the segment
    :type last_time_step: int, optional
    :param restart_flag: If ".true.", then this experiment is a restart. Note in Fortran notation
    :type restart_flag: str, optional
    :param output_feedback_files: Path to output model feedback files used for data assimilation
    :type output_feedback_files: str, optional
    :param iceberg_output_directory: Path to output iceberg trajectory files
    :type iceberg_output_directory: str, optional
    :param model_nemo_node_features: (Slurm-only) Constraints/features for the
                                    node
    :type model_nemo_node_features: str, optional
    :param orchestrator_port: port that the database will listen on
    :type orchestrator_port: int, optional
    :param orchestrator_interface: network interface bound to the database
    :type orchestrator_interface: str, optional
    :param orchestrator_nodes: number of orchestrator nodes to use
    :type orchestrator_nodes: int, optional
    :param orchestrator_nemo_node_features: node features requested for
                                       the orchestrator nodes
    :type orchestrator_nemo_node_features: str, optional
    :param configure_only: If True, only configure the experiment and return
                           the orchestrator and experiment objects
    :type configure_only: bool, optional
    """

    experiment = Experiment("NEMO-MEDITERR", launcher="local")
    nemo_model = create_nemo_model(
        experiment,
        nemo_num_nodes,
        nemo_tasks_per_node,
        nemo_node_features,
        xios_num_nodes,
        xios_tasks_per_node,
        xios_node_features,
        xios_exe,
        nemo_cfg_path,
        nemo_input_path,
        nemo_forcing_path
     )
    configure_nemo_model(
        nemo_model,
        job_number,
        first_time_step,
        last_time_step,
        restart_flag,
        restart_directory,
    )
    orchestrator = create_distributed_orchestrator(
        experiment,
        orchestrator_port,
        orchestrator_interface,
        orchestrator_nodes,
        orchestrator_nemo_node_features,
    )

    experiment.generate( nemo_model, orchestrator, overwrite=True )
    experiment.start(nemo_model, orchestrator, summary=True)
    experiment.stop(orchestrator)

if __name__ == "__main__":
    import fire
    log_to_file("/gpfswork/rech/eee/rote001/nemo4-imhotep-main/cfgs/MED025.L75-JZAA001/EXP_SMSIM/nemo_driver.log", log_level='debug')
    fire.Fire({
        "clustered":nemo_clustered_driver
    })
