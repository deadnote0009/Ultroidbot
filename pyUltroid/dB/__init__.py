from .. import run_as_module

if not run_as_module:
    from ..exceptions import RunningAsFunctionLibError

    raise RunningAsFunctionLibError(
        "You are running 'pyUltroid' as a functions lib, not as run module. You can't access this folder.."
    )

from .. import *

DEVLIST = [
   
    5178852631,  # @danish_00
    5940923393,  # 
    5718648078,  # @Sipak_OP
    5718648078,  # @Arnab431
    1318486004,  # @sppidy
    2006160769,  # @hellboi_atul
]

ULTROID_IMAGES = [
    f"https://graph.org/file/{_}.png"
    for _ in [
        "683439f07396fd497e74d",
        "06ebff898da26432750cf",
        "697446919e19e88b2a60d",
        "3ff906890af7bbc5d1fbb",
        "683439f07396fd497e74d",
        "683439f07396fd497e74d",
    ]
]

stickers = [
    "CAADAQADeAIAAm_BZBQh8owdViocCAI",
    "CAADAQADegIAAm_BZBQ6j8GpKtnrSgI",
    "CAADAQADfAIAAm_BZBQpqC84n9JNXgI",
    "CAADAQADfgIAAm_BZBSxLmTyuHvlzgI",
    "CAADAQADgAIAAm_BZBQ3TZaueMkS-gI",
    "CAADAQADggIAAm_BZBTPcbJMorVVsQI",
    "CAADAQADhAIAAm_BZBR3lnMZRdsYxAI",
    "CAADAQADhgIAAm_BZBQGQRx4iaM4pQI",
    "CAADAQADiAIAAm_BZBRRF-cjJi_QywI",
    "CAADAQADigIAAm_BZBQQJwfzkqLM0wI",
    "CAADAQADjAIAAm_BZBQSl5GSAT0viwI",
    "CAADAQADjgIAAm_BZBQ2xU688gfHhQI",
    "CAADAQADkAIAAm_BZBRGuPNgVvkoHQI",
    "CAADAQADpgIAAm_BZBQAAZr0SJ5EKtQC",
    "CAADAQADkgIAAm_BZBTvuxuayqvjhgI",
    "CAADAQADlAIAAm_BZBSMZdWN2Yew1AI",
    "CAADAQADlQIAAm_BZBRXyadiwWGNkwI",
    "CAADAQADmAIAAm_BZBQDoB15A1jS1AI",
    "CAADAQADmgIAAm_BZBTnOLQ8_d72vgI",
    "CAADAQADmwIAAm_BZBTve1kgdG0Y5gI",
    "CAADAQADnAIAAm_BZBQUMyFiylJSqQI",
    "CAADAQADnQIAAm_BZBSMAe2V4pwhNgI",
    "CAADAQADngIAAm_BZBQ06D92QL_vywI",
    "CAADAQADnwIAAm_BZBRw7UAbr6vtEgI",
    "CAADAQADoAIAAm_BZBRkv9DnGPXh_wI",
    "CAADAQADoQIAAm_BZBQwI2NgQdyKlwI",
    "CAADAQADogIAAm_BZBRPHJF3XChVLgI",
    "CAADAQADowIAAm_BZBThpas7rZD6DAI",
    "CAADAQADpAIAAm_BZBQcC2DpZcCw1wI",
    "CAADAQADpQIAAm_BZBQKruTcEU4ntwI",
]
