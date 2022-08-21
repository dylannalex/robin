class TaskSelector:
    TASK = {
        "process_scheduling": "t_ps",
        "paging": "t_p",
    }


class ProcessScheduling:
    GUIDE = {
        "round_robin": "g_rr",
        "shortest_job_first": "g_sjf",
        "shortest_remaining_time_next": "g_srtn",
        "first_come_first_served": "g_fcfs",
    }

    EXAMPLE = {
        "load_processes": "e_lp",
        "round_robin_time_slice_and_modification": "e_rrtsm",
    }

    EXPECTED_INPUT = {
        "processes": "ei_processes",
        "time_slice_and_modification": "ei_tsm",
    }


class Paging:
    GUIDE = {
        "translate_logical_to_real": "g_tlr",
        "real_address_length": "g_ral",
        "logical_address_length": "g_lal",
    }

    EXAMPLE = {
        "translate_logical_to_real": "e_tlr",
        "get_real_address": "e_gra",
        "real_address_length": "e_ral",
        "logical_address_length": "e_lal",
    }

    EXPECTED_INPUT = {
        "logical_address_and_page_size": "ei_laps",
        "page_frame": "ei_pf",
        "frame_number_and_size": "ei_fns",
        "page_number_and_size": "ei_pns",
    }
