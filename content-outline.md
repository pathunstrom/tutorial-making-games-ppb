1. Introduction - No more than 5 minutes
    1. Piper Thunstrom
    2. PPB
    3. Get installed
        1. Install python 3.7
        2. Create a virtual environment
        3. Install ppb in your virtual environment
        4. Piskel
2. Game 1 - A simple "shooter"
    1. Making a screen
        1. 2d Graphics
        2. An infinite loop
    2. Adding a sprite  - Goal: What a sprite is, how to build one.
        1. Modeling strategies
            1. ECS
            2. OO
        2. Class attributes
    3. Hooking up controls  - Goal: Keyboard controls
        1. Events
        2. Event handlers
        3. Flags
    4. Making projectiles  - Goal: Spawning sprites during the game instead of startup.
        1. Defining a new sprite
        2. Creating the sprite in an event handler
    5. Making something to target  - Goal: Collision detection.
        1. scene.get
        2. Basic collision detection
3. Game 2 - Virtual Pet
    1. Creating your pet  - Goal: A different way of modeling: subsystems
        1. What is a subsytem
            1. The API
            2. Adding to the engine
    2. Your pet gets hungry  - Goal: UI elements
        1. Define the events
        2. Add the stat to the subsystem.
        3. Add the UI button.
        4. Wire the button to drop the food.
        5. Simulate the food falling
        6. Throwing the event when the food is eaten.
    3. Saving and loading your game
        1. Add load code
        2. Add save code