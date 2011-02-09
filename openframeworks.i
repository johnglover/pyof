%module(directors="1") openframeworks
%{
    #define SWIG_FILE_WITH_INIT
    #include "../libs/openFrameworks/utils/ofTypes.h"
    #include "../libs/openFrameworks/video/ofQtUtils.h"
    #include "../libs/openFrameworks/utils/ofConstants.h"
    #include "../libs/openFrameworks/utils/ofMath.h"
    #include "../libs/openFrameworks/utils/ofUtils.h"
    #include "../libs/openFrameworks/communication/ofSerial.h"
    #include "../libs/openFrameworks/graphics/ofTexture.h"
    #include "../libs/openFrameworks/graphics/ofTrueTypeFont.h"
    #include "../libs/openFrameworks/graphics/ofGraphics.h"
    #include "../libs/openFrameworks/graphics/ofImage.h"
    #include "../libs/openFrameworks/app/ofAppRunner.h"
    #include "../libs/openFrameworks/app/ofBaseApp.h"
    #include "../libs/openFrameworks/sound/ofSoundStream.h"
    #include "../libs/openFrameworks/sound/ofSoundPlayer.h"
    #include "../libs/openFrameworks/video/ofVideoPlayer.h"
    #include "../libs/openFrameworks/video/ofVideoGrabber.h"
    #include "../addons/ofxThread/src/ofxThread.h"
%}
%feature("director");
%include "opengl.i"
%include "std_string.i"

// OS X
#define __APPLE_CC__
#define OF_VIDEO_CAPTURE_QUICKTIME
#define OF_VIDEO_PLAYER_QUICKTIME
// TODO: this method is declared in ofVideoPlayer.h but not defined anywhere.
// Can this be either removed or ignored?
%{ void ofVideoPlayer::qtGetFrameCount(Movie &m){} %}

%include "../libs/openFrameworks/utils/ofTypes.h"
%include "../libs/openFrameworks/video/ofQtUtils.h"
%include "../libs/openFrameworks/utils/ofConstants.h"
%include "../libs/openFrameworks/utils/ofMath.h"
%include "../libs/openFrameworks/utils/ofUtils.h"
%include "../libs/openFrameworks/communication/ofSerial.h"
%include "../libs/openFrameworks/graphics/ofTexture.h"
%include "../libs/openFrameworks/graphics/ofTrueTypeFont.h"
%include "../libs/openFrameworks/graphics/ofGraphics.h"
%include "../libs/openFrameworks/graphics/ofImage.h"
%include "../libs/openFrameworks/app/ofAppRunner.h"
%include "../libs/openFrameworks/app/ofBaseApp.h"
%include "../libs/openFrameworks/sound/ofSoundStream.h"
%include "../libs/openFrameworks/sound/ofSoundPlayer.h"
%include "../libs/openFrameworks/video/ofVideoPlayer.h"
%include "../libs/openFrameworks/video/ofVideoGrabber.h"
%include "../addons/ofxThread/src/ofxThread.h"
