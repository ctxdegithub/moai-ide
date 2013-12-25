'''OpenGL extension NV.fragment_program4

This module customises the behaviour of the 
OpenGL.raw.GL.NV.fragment_program4 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension builds on the common assembly instruction set
	infrastructure provided by NV_gpu_program4, adding fragment
	program-specific features.
	
	This extension provides interpolation modifiers to fragment program
	attributes allowing programs to specify that specified attributes be
	flat-shaded (constant over a primitive), centroid-sampled (multisample
	rendering), or interpolated linearly in screen space.  The set of input
	and output bindings provided includes all bindings supported by
	ARB_fragment_program.  Additional input bindings are provided to determine
	whether fragments were generated by front- or back-facing primitives
	("fragment.facing"), to identify the individual primitive used to generate
	the fragment ("primitive.id"), and to determine distances to user clip
	planes ("fragment.clip[n]").  Additionally generic input attributes allow
	a fragment program to receive a greater number of attributes from previous
	pipeline stages than possible using only the pre-defined fixed-function
	attributes.
	
	By and large, programs written to ARB_fragment_program can be ported
	directly by simply changing the program header from "!!ARBfp1.0" to
	"!!NVfp4.0", and then modifying instructions to take advantage of the
	expanded feature set.  There are a small number of areas where this
	extension is not a functional superset of previous fragment program
	extensions, which are documented in the NV_gpu_program4 specification.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/fragment_program4.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.NV.fragment_program4 import *
### END AUTOGENERATED SECTION