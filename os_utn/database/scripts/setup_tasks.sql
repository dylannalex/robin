/* Setup task types */
INSERT INTO task_type (name, id) VALUES ("ProcessesScheduling", 0);
INSERT INTO task_type (name, id) VALUES ("Paging", 1);

/* Setup processes scheduling tasks */
INSERT INTO task (name, id, task_type_id) VALUES ("RoundRobin", 0, 0);
INSERT INTO task (name, id, task_type_id) VALUES ("SJF", 1, 0);
INSERT INTO task (name, id, task_type_id) VALUES ("SRTN", 2, 0);
INSERT INTO task (name, id, task_type_id) VALUES ("FCFS", 3, 0);

/* Setup paging tasks */
INSERT INTO task (name, id, task_type_id) VALUES ("TranslateLogicalToReal", 4, 1);
INSERT INTO task (name, id, task_type_id) VALUES ("RealAddressLength", 5, 1);
INSERT INTO task (name, id, task_type_id) VALUES ("LogicalAddressLength", 6, 1);