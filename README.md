# Attentional capture or disengagement by neutral vs fearful distractors

## Import modules

Import the necessary Python modules in the `inline_script` item called 'modules'

## Define helper functions

In the `inline_script` item called 'functions'

## Define constant variables

In the `inline_script` item called 'constants'

*TODO:* height of the monitor in cm

## Define trial list

In the block loop (`loop_item` called 'block_loop').

### Independant variables that are manipulated / crossed:

- Emotional condition ("neutral" vs "fear"). Note that this refers to the *initial* emotional expression of the distractor face, that is, *before* the change
- Change condition ("change" vs "no_change")
- Target position (1,2,3,4,5 or 6, referring to the corresponding circles)

Resulting in a fully crossed 2 x 2 x 6 design (24 conditions). Each condition occurs twice within a given block. (So 48 trials per block.)

### Independent variables that are pseudo-random or dependent on other factors

These variables are set in the `inline_script` item called 'trial_properties'

- Distractor position (pseudorandom, with the restriciton that the distractor should not occur adjacent to the target)
- Face change (neutral changes to fear and vice versa, but only on change trials)
- Face stimulus ("F01"-"F04", "M01"-"M04"). *TODO:* drawn with or without replacement?
- The after-change face is always the same as the before-change face, for example, "F01_FE" changes to "F01_FE" (again, only on face trials)

## Trial sequence

1. Start drift correction (wait for steady fixation)
2. Start EyeLink recording
3. Show fixdot
    - trigger msg: `eyetracker.log('start_phase fixdot')`
4. Show placeholders
    - trigger msg: `eyetracker.log('start_phase placeholders')`
    - Sleep 1500 ms
5. Gap
    - trigger msg: `eyetracker.log('start_phase gap')`
    - Random interval between 150 and 250 ms
6. Show target
    - trigger msg: `eyetracker.log('start_phase target')`
7. Show distractor (simultaneously with event 6)
    - trigger msg: `eyetracker.log('start_phase distractor')`
8. Wait for saccade:
    - Criterion: an amplitude of half the eccentricity, for 5 samples in a row
9. Change face (on change trials only)
    - trigger msg: `eyetracker.log('start_phase change')`
    - Note that this trigger is sent regardless of whether the face actually changes or not
10. Sleep 1000 ms (as in Born & THeeuwes, 2010)
