#ifndef _MDR_
#define _MDR_

#ifndef MDR_DLL_EXPORT
#ifdef MDR_DLL_LIB
# define MDR_DLL_EXPORT __declspec(dllexport)
#else // MDR_DLL_LIB
# define MDR_DLL_EXPORT __declspec(dllimport)
#endif // MDR_DLL_LIB
#endif // MDR_DLL_EXPORT

#include <mex.h>

#ifdef __cplusplus
extern "C" {
#endif

void MDR_DLL_EXPORT execute( int nlhs, mxArray* plhs[], int nrhs, const mxArray* prhs[]);

#ifdef __cplusplus
}
#endif

#endif // _MRD_
