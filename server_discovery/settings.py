def init():
    global version
    global logger
    global irc_bot
    global irc_channel_bot
    global irc_channel_main
    global irc_nick
    global irc_server_name
    global irc_server_port
    global dir_assigned_services
    global log_file_name
    global run_services
    global run_services_running
    global upload
    global upload_running
    global services
    global running
    global standard_regex_video
    global standard_regex_live
    global target

    # variables to be changed
    version = 20160720.01
    irc_channel_bot = '#newsgbot'
    irc_channel_main = '#newsg'
    irc_nick = 'nd-arkive'
    irc_server_name = 'irc.underworld.no'
    irc_server_port = 6667
    dir_assigned_services = 'assigned_services'
    log_file_name = 'log.log'
    target = 'target'
    standard_regex_video = [r'^https?:\/\/[^\/]+\/.*vid(?:eo)?', r'^https?:\/\/[^\/]+\/.*[tT][vV]', r'^https?:\/\/[^\/]+\/.*movie']
    standard_regex_live = [r'^https?:\/\/[^\/]+\/.*live']

    # variables to be changed by script
    services = {}
    irc_bot = None
    logger = None
    run_services = None
    run_services_running = True
    upload = None
    upload_running = True
    running = True
