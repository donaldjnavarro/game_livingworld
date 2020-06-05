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
- Do weapons need to be distinct, or should all objects have things like weight and hardness and sharpness defined and then an attack action can use any object, or even your own body
- Should places be classes? Should instances of matter use their self.location field to store a loction instance? or just map to a location instance?
  - And how does this combine with "here" to map to the user's current location?
- Actors and Props are indistinguishable in design, but should places be a separate structure?

# TODO
- Need unique identifiers so multiple objects can be created with the same name
  