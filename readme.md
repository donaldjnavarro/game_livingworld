#  Virtualizing a World

## Design
- A collection of classes that inherit each other to define what methods are available to a thing created
    - Class Matter
    - Class Mind
    - Class Organic (Matter)
    - Class Plant (Organic)
    - Class Animal (Organic, Mind)
    - Class Mammal (Animal)
    - Class Sentient (Mind)
    - Class Humanoid
    - Class Human (Mammal, Humanoid, Sentient)

## Questions
- Actors and Props are indistinguishable in design, but should places be a separate class structure? How will this interact with matter instance locations?
- Do weapons need to be distinct, or should all objects have things like weight and hardness and sharpness defined and then an attack action can use any object, or even your own body

# Todo
- Need unique identifiers so multiple objects can be created with the same name
- Matter should have a weight field
- Animals have methods to interact with matter, if they have sufficient strength compared to the matter.weight  