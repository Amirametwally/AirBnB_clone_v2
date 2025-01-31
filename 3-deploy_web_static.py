#!/usr/bin/python3
"""script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env, local
from os.path import exists, isdir
from datetime import datetime


env.hosts = ["54.237.99.66", "34.202.159.136"]


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """distributes an archive to servers"""
    if not exists(archive_path):
        print("Archive does not exist.")
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}{}/".format(path, no_ext))
        run("sudo tar -xzf /tmp/{} -C {}{}/".format(file_n, path, no_ext))
        run("sudo rm /tmp/{}".format(file_n))
        run("sudo mv {0}{1}/web_static/* {0}{1}/".format(path, no_ext))
        run("sudo rm -rf {}{}/web_static".format(path, no_ext))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}{}/ /data/web_static/current".format(path, no_ext))
        if run("test -e /data/web_static/current").failed:
            print("Failed to create symlink.")
            return False
        return True
    except Exception as e:
        print("An error occurred during deployment: {}".format(str(e)))
        return False


def deploy():
    """creates and distributes archive to servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
