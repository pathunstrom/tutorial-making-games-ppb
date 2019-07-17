1. import/run
    - mention rendering contexts
    - raster graphics
2. add sprite
    - Not the animated images
    - ECS
    - OOP
3. add setup function
    - Tree structure of ppb games
4. add class attributes: velocity, speed, position
    - ppb allows defining defaults at class level
    - our init function also lets you set them at call time.
5. add on_key_pressed handler
    - The shape of an event handler
    - event definitions
6. modify velocity based on key_pressed function/define controls
    - Vectors!
    - keycodes
7. invert for key_released
8. Player.on_update
    - Update pattern
    - Game units
9. Projectile
    - size attribute
    - Same basic simulation, except we don't need to check for zero vector
    - Add it to setup function 
10. Shoot event
    - dataclasses
    - the signal function
