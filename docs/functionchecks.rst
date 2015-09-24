:mod:`simpleaudio.functionchecks`
=================================

.. module:: simpleaudio.functionchecks
   :synopsis: Provides tests of functionality by playing various test audio clips.

The :mod:`~simpleaudio.functionchecks` module contains a number of classes that all inherit 
from :class:`FunctionCheckBase` which provides :meth:`~FunctionCheckBase.run()` class method common to 
all function checks. These may be run individually with :meth:`~FunctionCheckBase.run()` 
or all test may be run with :func:`run_all()`.
   
Examples
--------

API
---

.. function::  run_all(countdown=3)

   Runs all function checks in succession. 

   :param int countdown: the number of seconds to pause before running each test
   
.. class:: FunctionCheckBase

   A base class for all function checks. 

.. method:: FunctionCheckBase.run(countdown=0)

   Runs a particular function check. 

   :param int countdown: the number of seconds to pause before running the test
   
.. class:: LeftRightCheck

   Checks stereo playback by first playing a note
   in the left channel only, then a different note in the
   right channel only.

.. class:: OverlappingCheck

   Checks overlapped playback by playing three different notes
   spaced approximately a half-second apart but still overlapping.

.. class:: RatesAndChannelsCheck

   Checks playback of mono and stereo audio at a subset of allowed sample rates and bit-depths.

.. class:: StopCheck

   Checks stopping playback by playing three different
   notes simultaneously and stopping two after approximately a half-second,
   leaving only one note playing for two more seconds.

.. class:: StopAllCheck

   Checks stopping playback of all audio by playing three different
   notes simultaneously and stopping all of them after approximately
   a half-second.

.. class:: IsPlayingCheck

   Checks functionality of the is_playing() method by
   calling during playback (when it should return True)
   and calling it again after all playback has stopped
   (when it should return False). The output is printed.

.. class:: WaitDoneCheck

   Checks functionality of the wait_done() method
   by using it to allow the three-note clip to play
   until finished (before attempting to stop playback).