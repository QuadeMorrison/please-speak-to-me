# please-speak-to-me
Please Speak to Me is a front end to the user to test a voice model produced by tacotron.

Tacotron is based on a sequence-to-sequence model, involving encoding the audio samples into
a numeric form. This numeric form is easier to translate into a data model that can be run
through several different neural networks. The data is then decoded into spectrograms which
is essentially a visual representatation of an audio file. Following some post processing
the spectrogram are converted into wav files. To learn more about this process you may
look into the following paper published by google.

To try this out yourself go to [please-speak-to-me](http://please-speak-to-me.herokuapp.com/)

[Tacotron paper](https://arxiv.org/pdf/1703.10135.pdf)

# Additional Learning Resources
[Speech Zone](http://www.speech.zone/)
* A collection of master level courses explaining how to synthesize a voice
  using hidden markov models and neural networks.

[Merlin](https://github.com/CSTR-Edinburgh/merlin)
* An open source library that implements an algorithm to synthesize a voice.
  Maintained by the authors of Speech Zone

[Idlak](https://github.com/idlak/idlak)
* An alternative to Merlin

[Tacotron implementation](https://github.com/coljamkop/tacotron)
* A fork of an implementation of tacotron. The original can be found [here](https://github.com/Kyubyong/tacotron)
  This fork is maintained for the purposes of this front end.
