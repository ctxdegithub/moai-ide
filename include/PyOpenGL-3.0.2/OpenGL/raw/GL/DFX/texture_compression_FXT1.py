'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_DFX_texture_compression_FXT1'
_p.unpack_constants( """GL_COMPRESSED_RGB_FXT1_3DFX 0x86B0
GL_COMPRESSED_RGBA_FXT1_3DFX 0x86B1""", globals())


def glInitTextureCompressionFxt1DFX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )