# 🏎️ Drag Race Simulator 🏎 ️

Drag Race Simulator is a simple application simulating communication with an electronic time tracking system for race cars. Written to simulate communication with backend app writen in PHP. 

## Features

- Simulation of races with various scenarios.
- False start handling with a specified probability.
- Calculating race times based on car parameters.
- Communication via WebSocket.

## Project Structure

- **models**: Class definitions for models such as `BaseCar` and `RaceResult`.
- **handlers**: Handling various race stages, such as start, false start, and crossing the finish line.
- **managers**: Managing race scenarios and their execution.
- **main.py**: The main entry point of the application.
