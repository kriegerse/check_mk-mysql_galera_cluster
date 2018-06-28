# check_mk-mysql_galera_cluster
A Check_MK plugin for checking the status of a galera cluster (based on http://galeracluster.com/documentation-webpages/monitoringthecluster.html)

The check parases the mysql output of the standard check_mk_agent for the presence of specific wsrep variables and status lines.

It will provide three single checks:

* MySQL Galera Cluster State
* MySQL Galera Node State
* MySQL Galera Replication Health

![services](documentation/check_mk_galera_cluster_services.png)

License: [GPLv2](LICENSE)

##
