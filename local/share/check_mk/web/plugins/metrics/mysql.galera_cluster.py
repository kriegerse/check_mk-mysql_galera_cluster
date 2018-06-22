
# define metrics color/unit 

# recv queue
metric_info["recv_queue"] = {
  "title":  _("Recv Queue CUR"),
  "unit":  "", 
  "help":  _("Current (instantaneous) length of the recv queue."),
  "color": "23/a",
}

metric_info["recv_queue_avg"] = {
  "title":  _("Recv Queue AVG"),
  "unit":  "", 
  "help":  _("Recv queue length averaged over interval since the last FLUSH STATUS command. Values considerably larger than 0.0 mean that the node cannot apply write-sets as fast as they are received and will generate a lot of replication throttling."),
  "color": "44/b",
}

metric_info["recv_queue_max"] = {
  "title":  _("Recv Queue MAX"),
  "unit":  "",
  "help":  _("The maximum length of the recv queue since the last FLUSH STATUS command."),
  "color": "21/a",
}

metric_info["recv_queue_min"] = {
  "title":  _("Recv Queue MIN"),
  "unit":  "",
  "help":  _("The minimum length of the recv queue since the last FLUSH STATUS command."),
  "color": "31/a",
}


# send queue
metric_info["send_queue"] = {
  "title":  _("Send Queue CUR"),
  "unit":  "", 
  "help":  _("Current (instantaneous) length of the send queue."),
  "color": "23/a",
}

metric_info["send_queue_avg"] = {
  "title":  _("Send Queue AVG"),
  "unit":  "",
  "help":  _("Send queue length averaged over time since the last FLUSH STATUS command. Values considerably larger than 0.0 indicate replication throttling or network throughput issue."),
  "color": "44/b",
}

metric_info["send_queue_max"] = {
  "title":  _("Send Queue MAX"),
  "unit":  "",
  "help":  _("The maximum length of the send queue since the last FLUSH STATUS command."),
  "color": "21/a",
}

metric_info["send_queue_min"] = {
  "title":  _("Send Queue MIN"),
  "unit":  "",
  "help":  _("The minimum length of the send queue since the last FLUSH STATUS command."),
  "color": "31/a",
}

# flow control
metric_info["flow_control_paused"] = {
  "title": _("Flow Control paused"),
  "unit":  "s",
  "help":  _("The fraction of time since the last FLUSH STATUS command that replication was paused due to flow control. In other words, how much the slave lag is slowing down the cluster."),
  "color": "23/a",
}

metric_info["flow_control_recv"] = {
  "title": _("Flow Control Recv"),
  "unit":  "",
  "help":  _("Returns the number of FC_PAUSE events the node has received, including those the node has sent between two measurements (COUNTER)"),
  "color":  "21/a",
}

metric_info["flow_control_sent"] = {
  "title": _("Flow Control Sent"),
  "unit":  "",
  "help":  _("Returns the number of FC_PAUSE events the node has sent between two measurements (COUNTER)"),
  "color":  "21/b",
}


# cert deps distance
metric_info["cert_deps_distance"] = {
   "title": _("Cert deps distance"),
   "unit": "",
   "help":  _("Average distance between highest and lowest seqno value that can be possibly applied in parallel (potential degree of parallelization)."),
   "color": "23/b",
}




# define perometer
perfometer_info.append(("dual", [
 { 
   "type":	"linear",
   "segments":  [ "recv_queue" ],
 },
 {
   "type":	"linear",
   "segments":  [ "send_queue" ],
 }
]))



# define graphs 

# Graph Recv Queue 
graph_info.append({
   "title"   : _("Local Recive Queue"),
   "metrics" : [ 
      ( "recv_queue_avg",   "area" ), 
      ( "recv_queue",       "line" ), 
      ( "recv_queue_max",   "line" ),
      ( "recv_queue_min",   "line" ),
   ],
   "optional_metrics": [
       "recv_queue_max",
       "recv_queue_min",
   ],
   "scalars": [
       ( "recv_queue_avg:warn", _("warn")),
       ( "recv_queue_avg:crit", _("crit")),
   ],
})

# Graph Send Queue 
graph_info.append({
   "title"   : _("Local Send Queue"),
   "metrics" : [ 
      ( "send_queue_avg",   "area" ),
      ( "send_queue",       "line" ),
      ( "send_queue_max",   "line" ),
      ( "send_queue_min",   "line" ),
   ],
   "optional_metrics": [
       "send_queue_max", 
       "send_queue_min", 
   ],
   "scalars": [
       "send_queue_avg:warn",
       "send_queue_avg:crit",
   ],
})


# Graph Flow Control Paused
graph_info.append( {
   "title":       _("Flow Control Paused"),
   "metrics":      [
       ( "flow_control_paused", "area" ),
   ],
   "scalars": [
       "flow_control_paused:warn",
       "flow_control_paused:crit",
   ],
})


# Graph Flow Control Commands 
graph_info.append( {
   "title":       _("Flow Control Recv/Sent"),
   "metrics":      [
       ( "flow_control_recv",   "line" ),
       ( "flow_control_sent",   "-line" ),
   ],
})

## Cert Deps Distance 
graph_info.append({
   "title": _("Cert Deps Distance"),
   "metrics":  [
       ( "cert_deps_distance", "area" ),
   ],
})



