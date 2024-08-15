#!/usr/bin/env python

APPNAME = 'PixelFlasher'
CONFIG_FILE_NAME = 'PixelFlasher.json'
VERSION = '1.0.0.0'
SDKVERSION = '33.0.3'
MAIN_WIDTH = 1400
MAIN_HEIGHT = 1040
MAGISK_WIDTH = 1400
MAGISK_HEIGHT = 1040
PIF_WIDTH = 1150
PIF_HEIGHT = 840
POS_X = 40
POS_Y = 40
KNOWN_INIT_BOOT_DEVICES = ['panther', 'cheetah', 'lynx', 'tangorpro', 'felix', 'shiba', 'husky', 'aurora', 'eos', 'akita']
KNOWN_BAD_MAGISKS = ['7dbfba76:25207', 'e5641d5b:25208', '2717feac:25209', '981ccabb:25210', '69529ac5:25211', 'e2545e57:26001', '26.0:26000', 'a8c4a33e:26103']
FACTORY_IMAGES_FOR_PIXEL_DEVICES = 'https://developers.google.com/android/images'
FULL_OTA_IMAGES_FOR_PIXEL_DEVICES = 'https://developers.google.com/android/ota'
FACTORY_IMAGES_FOR_WATCH_DEVICES = 'https://developers.google.com/android/images-watch'
FULL_OTA_IMAGES_FOR_WATCH_DEVICES = 'https://developers.google.com/android/ota-watch'
FACTORY_IMAGES_FOR_BETA = 'https://developer.android.com/about/versions/15/download'
FULL_OTA_IMAGES_FOR_BETA = 'https://developer.android.com/about/versions/15/download-ota'
PIF_UPDATE_URL = 'https://raw.githubusercontent.com/chiteroman/PlayIntegrityFix/main/update.json'
OSM0SIS_PIF_UPDATE_URL = 'https://raw.githubusercontent.com/osm0sis/PlayIntegrityFork/main/update.json'
TRICKYSTORE_UPDATE_URL = 'https://raw.githubusercontent.com/5ec1cff/TrickyStore/main/update.json' # non-existent, just a placeholder
PIF_JSON_PATH = '/data/adb/pif.json'
XIAOMI_URL = "https://sourceforge.net/projects/xiaomi-eu-multilang-miui-roms/rss?path=/xiaomi.eu/Xiaomi.eu-app"
FREEMANURL = "https://codeload.github.com/TheFreeman193/PIFS/zip/refs/heads/main"
SCRCPYURL = "https://github.com/Genymobile/scrcpy/releases/latest"
PIXEL_WATCHES = ['eos', 'aurora', 'r11', 'r11btwifi']
# https://xdaforums.com/t/module-play-integrity-fix-safetynet-fix.4607985/page-518#post-89308909
BANNED_KERNELS = [
    '-AICP',
    '-arter97',
    '-blu_spark',
    '-CAF',
    '-cm-',
    '-crDroid',
    '-crdroid',
    '-CyanogenMod',
    '-Deathly',
    '-EAS-',
    '-eas-',
    '-ElementalX',
    '-Elite',
    '-franco',
    '-hadesKernel',
    '-Lineage-',
    '-lineage-',
    '-LineageOS',
    '-lineageos',
    '-mokee'
    '-MoRoKernel',
    '-Noble',
    '-Optimus',
    '-SlimRoms',
    '-Sultan',
    '-sultan'
]
MAGISK_PKG_NAME = 'com.topjohnwu.magisk'
MAGISK_ALPHA_PKG_NAME = 'io.github.vvb2060.magisk'
MAGISK_DELTA_PKG_NAME = 'io.github.huskydg.magisk'
KERNEL_SU_PKG_NAME = 'me.weishu.kernelsu'
APATCH_PKG_NAME = 'me.bmax.apatch'
ZYGISK_NEXT_UPDATE_URL = 'https://api.nullptr.icu/android/zygisk-next/static/update.json'
