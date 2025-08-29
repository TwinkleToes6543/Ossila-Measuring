#ifndef LIBSPECTR_H
#define LIBSPECTR_H

#include <stdint.h> // Use standard uint types

// Platform-specific export macros
#if defined(_WIN32)
#ifdef LIBSHARED_AND_STATIC_STATIC_DEFINE
#define LIBSHARED_AND_STATIC_EXPORT
#else
#ifdef spectrlib_shared_EXPORTS
#define LIBSHARED_AND_STATIC_EXPORT __declspec(dllexport)
#else
#define LIBSHARED_AND_STATIC_EXPORT __declspec(dllimport)
#endif
#endif
#else
#if __GNUC__ >= 4
#define LIBSHARED_AND_STATIC_EXPORT __attribute__((visibility("default")))
#else
#define LIBSHARED_AND_STATIC_EXPORT
#endif
#endif

// Error codes
#define OK 0
#define CONNECT_ERROR_WRONG_ID 500
#define CONNECT_ERROR_NOT_FOUND 501
#define CONNECT_ERROR_FAILED 502
#define DEVICE_NOT_INITIALIZED 503
#define WRITING_PROCESS_FAILED 504
#define READING_PROCESS_FAILED 505
#define WRONG_ANSWER 506
#define GET_FRAME_REMAINING_PACKETS_ERROR 507
#define NUM_OF_PACKETS_IN_FRAME_ERROR 508
#define INPUT_PARAMETER_NOT_INITIALIZED 509
#define READ_FLASH_REMAINING_PACKETS_ERROR 510

#ifdef __cplusplus
extern "C"
{
#endif

    // Function declarations
    LIBSHARED_AND_STATIC_EXPORT int connectToDevice(const char *serialNumber);
    LIBSHARED_AND_STATIC_EXPORT void disconnectDevice();
    LIBSHARED_AND_STATIC_EXPORT int setAcquisitionParameters(uint16_t numOfScans, uint16_t numOfBlankScans, uint8_t scanMode, uint32_t timeOfExposure);
    LIBSHARED_AND_STATIC_EXPORT int setExposure(uint32_t timeOfExposure, uint8_t force);
    LIBSHARED_AND_STATIC_EXPORT int setFrameFormat(uint16_t numOfStartElement, uint16_t numOfEndElement, uint8_t reductionMode, uint16_t *numOfPixelsInFrame);
    LIBSHARED_AND_STATIC_EXPORT int getFrameFormat(uint16_t *numOfStartElement, uint16_t *numOfEndElement, uint8_t *reductionMode, uint16_t *numOfPixelsInFrame);
    LIBSHARED_AND_STATIC_EXPORT int triggerAcquisition();
    LIBSHARED_AND_STATIC_EXPORT int setExternalTrigger(uint8_t enableMode, uint8_t signalFrontMode);
    LIBSHARED_AND_STATIC_EXPORT int setOpticalTrigger(uint8_t enableMode, uint16_t pixel, uint16_t threshold);
    LIBSHARED_AND_STATIC_EXPORT int getStatus(uint8_t *statusFlags, uint16_t *framesInMemory);
    LIBSHARED_AND_STATIC_EXPORT int clearMemory();
    LIBSHARED_AND_STATIC_EXPORT int getFrame(uint16_t *framePixelsBuffer, uint16_t numOfFrame);
    LIBSHARED_AND_STATIC_EXPORT int eraseFlash();
    LIBSHARED_AND_STATIC_EXPORT int readFlash(uint8_t *buffer, uint32_t absoluteOffset, uint32_t bytesToRead);
    LIBSHARED_AND_STATIC_EXPORT int writeFlash(uint8_t *buffer, uint32_t offset, uint32_t bytesToWrite);
    LIBSHARED_AND_STATIC_EXPORT int resetDevice();
    LIBSHARED_AND_STATIC_EXPORT int detachDevice();
    LIBSHARED_AND_STATIC_EXPORT int getAcquisitionParameters(uint16_t *numOfScans, uint16_t *numOfBlankScans, uint8_t *scanMode, uint32_t *timeOfExposure);
    LIBSHARED_AND_STATIC_EXPORT int setAllParameters(uint16_t numOfScans, uint16_t numOfBlankScans, uint8_t scanMode, uint32_t timeOfExposure, uint8_t enableMode, uint8_t signalFrontMode);

#ifdef __cplusplus
}
#endif

#endif // LIBSPECTR_H