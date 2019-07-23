1. Set up a package
    * folder
    * setup.py
        * Author
        * packages
        * install_requires
    * pip install -e .
2. Get a window setup
    * \_\_main__.py
    * get a window open
    * add an entry point
3. Add our sprite
    * make a sprite
    * make a scene
4. Stats Subsystem
    * make system
    * on_render debug
    * hook into the engine
5. Make the pet grow
    * Add an event.
    * Raise event when age changes
    * Capture the event on your pet.
    * math.log
6. Make the Pet get hungry
    * Add GrowHungry event
    * Add hunger and hunger counter
    * Throw event when hunger changes
7. Communicate hunger
    * Thought class
        * Movement
        * Image
        * Killing sprite
    * Capture event in Pet
    * Create Thought with correct image
8. Add food
    * Food class
    * Collision with Pet
    * Food button
        * on_button_pressed
        * Creating food
9. Satiate your pet
    * FoodEaten event
    * Signal FoodEaten when pet eats food
    * Capture FoodEaten in PetStats to raise hunger score.
10. Save your pet
    * on_quit handler
    * convert pet stats to dictionary
    * json.dump to a save file.
11. Load your Pet
    * Add try:except to the \_\_init__
    * with open("save_file.json"): json.load
    * Set stats
    * signal hunger and age