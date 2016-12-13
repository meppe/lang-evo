#!/bin/bash
docker rm ros-lang-evo-kinetic_world
xhost +local:`docker inspect --format='{{ .Config.Hostname }}' ros-lang-evo-kinetic_world` 
nvidia-docker run \
--rm \
-it \
--workdir="//opt/lang-evo" \
--env="DISPLAY" \
--env="QT_X11_NO_MITSHM=1" \
--volume="/$(pwd):/opt/lang-evo" \
--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
--name ros-lang-evo-kinetic_world \
--entrypoint "/entrypoint.sh" \
meppe78/ros-lang-evo-kinetic-xenial \
bash
# roslaunch ros_cqi run_gazebo_darwin_demo.launch
# roslaunch ros_cqi run_gazebo_darwin_empty.launch
# roslaunch ros_cqi spawn_darwin.launch
# rosrun ros_cqi run_interface.py robot=darwin
xhost -local:`docker inspect --format='{{ .Config.Hostname }}' ros-lang-evo-kinetic_world`
