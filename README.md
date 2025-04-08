# Go2 Front Camera Feed

## Package Structure

```
my_ros2_ws/src/all_launch_go2/
├── all_launch_go2/
│   ├── __init__.py
├── launch/
│   └── go2_full_launch.launch.py # Launch file
├── resource/
│   └── all_launch_go2              # Marker file for package discovery
├── package.xml
├── setup.py
└── setup.cfg
```

## Dependencies

- ROS2 Foxy
- Python 3

## Usage

1. Single launch file for Go2 Navigation Project:
   ```bash
   ros2 launch all_launch_go2 go2_full_launch.launch.py
   ```
