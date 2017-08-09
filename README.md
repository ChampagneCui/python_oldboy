创建jpserver数据库使用utf8mb4字符串
python3 bin/jpserver.py --syncdb
python3 bin/jpserver.py --create_users=YAML/new_user.yml
python3 bin/jpserver.py --create_remoteusers=YAML/new_remoteusers.yml
python3 bin/jpserver.py --create_hosts=YAML/new_hosts.yml
python3 bin/jpserver.py --create_groups=YAML/new_groups.yml
python3 bin/jpserver.py --create_bindhosts=YAML/new_bindhosts.yml
