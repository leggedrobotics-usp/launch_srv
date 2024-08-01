<!-- <p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p> -->

<h1 align="center">launch_srv</h1>

<div align="center">

  [![GitHub issues](https://img.shields.io/github/issues/leggedrobotics-usp/launch_srv)](https://github.com/leggedrobotics-usp/launch_srv/issues)
  ![GitHub pull requests](https://img.shields.io/github/issues-pr/leggedrobotics-usp/launch_srv)
  [![GitHub forks](https://img.shields.io/github/forks/leggedrobotics-usp/launch_srv)](https://github.com/leggedrobotics-usp/launch_srv/network)
  [![GitHub stars](https://img.shields.io/github/stars/leggedrobotics-usp/launch_srv)](https://github.com/leggedrobotics-usp/launch_srv/stargazers)
  [![GitHub license](https://img.shields.io/github/license/leggedrobotics-usp/launch_srv)](https://github.com/leggedrobotics-usp/launch_srv/blob/main/LICENSE)

</div>

---

<p align="center"> A ROS2 package for calling launch files from a ROS service
    <br>
</p>

ROS version | Branch
-- | --
ROS2 | [ros2](https://github.com/leggedrobotics-usp/launch_srv/tree/ros2)
ROS1 | [ros1](https://github.com/leggedrobotics-usp/launch_srv/tree/ros1)

## 📝 Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Feature requests](#feature_requests)
- [Contributing](#contributing)
- [Author](#author)

## 🧐 About <a name = "about"></a>

**launch_srv** is a ROS package that provides:

- A service definition (Launch.srv) for calling launch files;
- A service server (launch_server.py) that implements this call;
- A launch file (foxglove.launch.py) that launches both the service server and [foxglove_bridge](https://github.com/foxglove/ros-foxglove-bridge).

## 🏁 Getting Started <a name = "getting_started"></a>
This repo is a standard ROS2 package (ament_cmake).

### 🛠 Prerequisites

- A ROS2 workspace (colcon)
    - See [this tutorial](https://docs.ros.org/en/rolling/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html) to learn how to create your own workspace.

- Foxglove bridge
    - ```bash
      sudo apt install ros-<distro>-foxglove-bridge
      ```

### 💻 Installing

As mentioned above, this repo is a standard ROS2 package. Thus, you simply have to clone it inside your workspace's **src** directory, making sure to use the **ros2** branch.

```bash
cd <path_to_your_ros2_ws>/src
git clone -b ros2 https://github.com/leggedrobotics-usp/launch_srv.git
```

Then, use **colcon** to build.

```bash
cd <path_to_your_ros2_ws>
colcon build --symlink-install
```

## 🎈 Usage <a name="usage"></a>

Run the service server:

```bash
ros2 run launch_srv launch_server.py
```

Each service call will trigger the corresponding launch file on a separate process. Configure the inputs as follows:

- ```package_name``` (string): the name of the package that contains the desired launch file;
- ```launch_file``` (string): the launch file name (complete, with extension);
- ```parameters``` (string): if necessary, input the parameter list;
- ```terminate``` (boolean): set to ```false``` to start the launch process, or ```true``` to terminate it.

If you want to call the service using Foxglove Studio, use the included launch file instead:

```bash
ros2 launch launch_srv foxglove.launch.py
```

## 🔋 Feature requests <a name="feature_requests"></a>

Want a new feature? Open an *Enhancement* issue describing it.

## 🤝 Contributing <a name="contributing"></a>

- Fork the repo
  - <https://github.com/leggedrobotics-usp/launch_srv/fork>
- Check out a new branch (from the **ros2** branch) and name it to what you intend to do:
  - ````bash
    git checkout -b BRANCH_NAME
    ````
- Commit your changes
  - Please provide a git message that explains what you've done;
  - Commit to the forked repository.
    ````bash
    git commit -m "A short and relevant message"
    ````
- Push to the branch
  - ````bash
    git push origin BRANCH_NAME
    ````
- Make a pull request!

## ✍️ Author <a name = "author"></a>

<a href="https://github.com/Vtn21">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/13922299?s=460&u=2e2554bb02cc92028e5cba651b04459afd3c84fd&v=4" width="100px;" alt=""/>
 <br />
 <sub><b>Victor T. N. 🤖</b></sub></a>

Made with ❤️ by [@Vtn21](https://github.com/Vtn21)

<!-- [![Gmail Badge](https://img.shields.io/badge/-victor.noppeney@usp.br-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:victor.noppeney@usp.br)](mailto:victor.noppeney@usp.br) -->

<!-- -  - Idea & Initial work -->

<!-- See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project. -->