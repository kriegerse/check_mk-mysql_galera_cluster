
# define metrics color/unit 
metric_info["recv_queue"] = {
  "title":  _("WSREP Local Recive Queue"),
  "unit":  "", 
  "color": "#90D4A9",
}

metric_info["recv_queue_avg"] = {
  "title":  _("WSREP Local Recive Queue AVG"),
  "unit":  "", 
  "color": "#FC2D80",
}

metric_info["recv_queue_max"] = {
  "title":  _("WSREP Local Recive Queue MAX"),
  "unit":  "",
  "color": "#FC2D80",
}

metric_info["recv_queue_min"] = {
  "title":  _("WSREP Local Recive Queue MIN"),
  "unit":  "",
  "color": "#FC2D80",
}


metric_info["send_queue"] = {
  "title":  _("WSREP Local Send Queue"),
  "unit":  "", 
  "color": "#3A9AD6",
}


# define perometer
perfometer_info.append(("stacked", [
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
   "title"   : _("WSREP Local Recive Queue - merged"),
   "metrics" : [ 
      ( "recv_queue", "line"), 
      ( "recv_queue_avg", "line"),
   ], 
})

