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
    - Class Weapon (Body)

## Questions
- Do weapons need to be distinct, or should all objects have things like weight and hardness and sharpness defined and then an attack action can use any object, or even your own body
- Do we need multiple cross sections of class definitions? Type (mammals, reptiles) vs Aspects (hands, speech)

# TODO
- Need unique identifiers so multiple objects can be created with the same name
  