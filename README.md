# Attentional capture or disengagement by neutral vs fearful distractors

## Import modules

Import the necessary Python modules in the `inline_script` item called 'modules'

## Define helper functions

In the `inline_script` item called 'functions'

## Define constant variables

In the `inline_script` item called 'constants'

## Define trial list

In the block loop (`loop_item` called 'block_loop').

### Independant variables that are manipulated / crossed:

- Emotional condition ("neutral" vs "fear")
- Change condition ("change" vs "no_change")
- Target position (1,2,3,4,5 or 6, referring to the corresponding circles)

Resulting in a fully crossed 2 x 2 x 6 design (24 conditions)

### Independent variables that are pseudo-random or dependent on other factors

- Distractor position (pseudorandom, with the restriciton that the distractor should not occur adjacent to the target)
- Face change (neutral changes to fear and vice versa, but only on change trials)
- Face stimulus ("F01"-"F04", "M01"-"M04"), drawn with or without replacement?
- The after-change face is always the same as the before-change face, for example, "F01_FE" changes to "F01_FE" (again, only on face trials)
