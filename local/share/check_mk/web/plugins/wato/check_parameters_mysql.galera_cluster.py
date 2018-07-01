#!/usr/bin/env python


# MySQL Galera Replication Health (mysql.galera_cluster_repl_health)
register_check_parameters(
   subgroup_applications,
   'galera_repl_health',
   _("MySQL Galera Replication Health"),
   Dictionary(
      help = _("Monitor the Cluster Replication Health"),
      elements = [
         ( "wsrep_local_recv_queue_avg",
            Tuple(
               title = "Recv queue length average", 
               help = _("Recv queue length averaged over interval since the last FLUSH STATUS command. "
                        "Values considerably larger than 0.0 mean that the node cannot apply write-sets as fast as they are received and will generate a lot of replication throttling."),
               elements = [
                  Float( title = _("Warning at/above"), default_value=0.5  ) ,
                  Float( title = _("Critical at/above"), default_value=1.0  ) ,
               ],
            ),
         ),
         ( "wsrep_local_send_queue_avg",
            Tuple(
               title = "Send queue length average",  
               help = _("Send queue length averaged over time since the last FLUSH STATUS command."
                        "Values considerably larger than 0.0 indicate replication throttling or network throughput issue."),
               elements = [
                  Float( title = _("Warning at/above"), default_value=0.5  ) ,
                  Float( title = _("Critical at/above"), default_value=1.0  ) ,
               ],
            ),
         ),
         ( "wsrep_flow_control_paused",
            Tuple(
               title = "Flow control paused",
               help = _("The fraction of time since the last FLUSH STATUS command that replication was paused due to flow control. "
                        "In other words, how much the slave lag is slowing down the cluster"),
               elements = [
                  Float( title = _("Warning at/above"), unit = _("seconds"), default_value=0.5  ) ,
                  Float( title = _("Critical at/above"), unit = _("seconds"), default_value=0.7  ) ,
               ],
            ),
         ),
      ],
   ),
   TextUnicode(
       title = _("Instance"),
       help  = _("Only needed if you have multiple MySQL Galera Instances on one server"),
   ),
   "dict",
)


# MySQL Node State (mysql.galera_cluster_node_state)
register_check_parameters(
   subgroup_applications,
   "galera_node_state",
   _("MySQL Galera Node State"),
   Dictionary(
      help = _("Monitor the Cluster Node state"),
      elements = [ 
         ( "wsrep_local_state_comment",
 	   TextUnicode(
              title = _("wsrep_local_state_comment"),
              help  = _("Shows the node state in a human readable format. "
                        "When the node is part of the Primary Component, the typical return values are Joining, Waiting on SST, Joined, Synced or Donor. "
                        "In the event that the node is part of a nonoperational component, the return value is Initialized. "
                        "Normaly you want to keep 'Initialized' (the relevant value to alert on)."),
              default_value = "Initialized",
           ),
         ),
         ( "wsrep_ready",
           TextUnicode(
              title = _("wsrep_ready"),
              help = _("Shows whether the node can accept queries. "
                       "When the node returns a value of ON it can accept write-sets from the cluster. "
                       "When it returns the value OFF, almost all queries fail with the error: 'ERROR 1047 (08501) Unknown Command'"
                       "Normally you want to keep ON, the default."),
              default_value = "On",
           )
         ),
         ( "wsrep_connected",
           TextUnicode(
              title = _("wsrep_connected"),
              help  = _("Shows whether the node has network connectivity with any other nodes. "
                        "When the value is ON, the node has a network connection to one or more other nodes forming a cluster component. When the value is OFF, the node does not have a connection to any cluster components. "
                        "Normally you want to keep ON, the default."),
              default_value = "On",
           ),
         ),
      ],
   ),
   TextUnicode(
       title = _("Instance"),
       help  = _("Only needed if you have multiple MySQL Galera Instances on one server"),
   ),
   "dict",
)

# MySQL Cluster State (mysql.galera_cluster)
register_check_parameters(
   subgroup_applications,
   "galera_cluster_state",
   _("MySQL Galera Cluster State"),
   Dictionary(
      help = _("This check monitors the current state of the Cluster"),
      elements= [
         ( "wsrep_cluster_size",
           Tuple(
              title = _("Number of Members of the Cluster"),
              help = _("Monitor the number of members in the cluster."),
              elements = [
                 Integer(title = _("Expected"), unit = _("members"), default_value = 4,
                         help = _("Defines the expected default size of the cluster when all members are present."), 
                 ),
                 Integer(title = _("Warning at/below"), unit = _("members"), default_value = 4,
                         help = _("Show a warning when the number of cluster members is at or below this threshold."),
                 ),
                 Integer(title = _("Critical at/below"), unit = _("members"), default_value = 3,
                         help = _("Show a critical state when the number of cluster members is at or below this threshold."),
                 ),
              ],
           ),
         ),
         ( "wsrep_cluster_status",
           TextUnicode(
              title = _("Expected Cluster Status"), 
              default_value = _("Primary"),
              help = _("Cluster Node component status. Possible values are 'Primary' (primary group configuration, quorum present), " 
                       "'Non_primary' (non-primary group configuration, quorum lost) or "
                       "'Disconnected' (not connected to group, retrying). "
                       "Normally you want keep PRIMARY (the default)."),
           ),
         ),
      ],
   ),
   TextUnicode(
       title = _("Instance"),
       help  = _("Only needed if you have multiple MySQL Galera Instances on one server"),
   ),
   "dict",
)

