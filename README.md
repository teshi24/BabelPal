# BabelPal - Pepper as an Interpreter
Dieses Repo enthält eine Pepperimplementation, welche den Roboter zum Dolmetscher zwischen zwei Personen macht.

Eine genauere Dokumentation über die Funktionalitäten ist in [documentation.md](documentation.md) zu finden.

## Prerequisites
- Virtual Machine with Windows and Python 2.7.13 - 32 bits version
- `pepper/babelpal/.env` file with TRANSLATION_SERVICE_AVAILABLE=False / True (translation service runs with python 3, start it outside of the VM. When setting it to False, a Mockservice is started)

## Settings
Ensure, that the IPs are correctly configured in [pepper/babelpal/interpreting_robot.py](pepper/babelpal/interpreting_robot.py).
Pepper tells you its IP when Pepper is awake and you press its chest button.

## Start-up

1. Start pepper
2. Connect to the `robo-duckie` network, ask your prof for the password.
3. In your VM, use the network adapter **bridged** (VM > Settings > Network Adapter).
4. Run [pepper/babelpal/main.py](pepper/babelpal/main.py) in the VM - don't worry when Pepper shuts down, it will come back up. The start-up script disables automatic life mode which requires a restart.
5. On your own machine, start the translation service by running [speech_translation/app.py](speech_translation/app.py).
6. Pepper is ready to start a conversation :)