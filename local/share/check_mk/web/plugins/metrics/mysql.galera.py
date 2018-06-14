
# define metrics color/unit 

# recv queue
metric_info["recv_queue"] = {
  "title":  _("Recv Queue CUR"),
  "unit":  "", 
  "help":  "metric help for recv_queue",
  "color": "23/a",
}

metric_info["recv_queue_avg"] = {
  "title":  _("Recv Queue AVG"),
  "unit":  "", 
  "color": "44/b",
}

metric_info["recv_queue_max"] = {
  "title":  _("Recv Queue MAX"),
  "unit":  "",
  "color": "21/a",
}

metric_info["recv_queue_min"] = {
  "title":  _("Recv Queue MIN"),
  "unit":  "",
  "color": "31/a",
}


# send queue
metric_info["send_queue"] = {
  "title":  _("Send Queue"),
  "unit":  "", 
  "color": "23/a",
}

metric_info["send_queue_avg"] = {
  "title":  _("Send Queue AVG"),
  "unit":  "",
  "color": "44/b",
}

metric_info["send_queue_max"] = {
  "title":  _("Send Queue MAX"),
  "unit":  "",
  "color": "21/a",
}

metric_info["send_queue_min"] = {
  "title":  _("Send Queue MIN"),
  "unit":  "",
  "color": "31/a",
}

# flow control
metric_info["flow_control_paused"] = {
  "title": _("Flow Control paused"),
  "unit":  "",
  "color": "23/a",
}

# cert deps distance
metric_info["cert_deps_distance"] = {
   "title": _("Cert deps distance"),
   "unit": "",
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
      ( "recv_queue",       "area" ), 
      ( "recv_queue_max",   "line" ),
      ( "recv_queue_min",   "line" ),
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
      ( "send_queue",       "area" ),
      ( "send_queue_max",   "line" ),
      ( "send_queue_min",   "line" ),
   ],
   "scalars": [
       "send_queue_avg:warn",
       "send_queue_avg:crit",
   ],
})


# Graph Flow Control
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

# Cert Deps Distance 
graph_info.append({
   "title": _("Cert Deps Distance"),
   "metrics":  [
       ( "cert_deps_distance", "area" ),
   ],
})



