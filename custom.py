# Generated using https://godot-build-options-generator.github.io
# Optimized for minimal Android so size

production = "yes"
optimize = "size"

# Core feature disables
disable_audio_3d = "yes"      # Disables only 3D audio (AudioStreamPlayer3D, AudioListener3D)
disable_debugger = "yes"
disable_movie_writer = "yes"
disable_advanced_gui = "yes"
disable_physics_2d = "yes"
disable_physics_3d = "yes"
disable_xr = "yes"
disable_navigation_2d = "yes"
disable_navigation_3d = "yes"
deprecated = "no"

# Optional features
minizip = "no"
brotli = "no"
vulkan = "no"

# Builtin libraries
builtin_zstd = "no"       # Disabled - compression.cpp uses ZSTD_ENABLED macro
builtin_zlib = "yes"      # Required for compression (core feature)

# These can be "no" if corresponding modules are disabled
builtin_glslang = "no"    # OK if module_glslang_enabled = no
builtin_enet = "no"       # OK if module_enet_enabled = no
builtin_wslay = "no"      # OK if module_websocket_enabled = no
builtin_libwebp = "no"    # OK if module_webp_enabled = no
builtin_pcre2 = "no"      # OK if module_regex_enabled = no
builtin_pcre2_with_jit = "no"
builtin_rvo2_2d = "no"    # OK if navigation disabled
builtin_rvo2_3d = "no"    # OK if navigation disabled
builtin_embree = "no"     # OK if raycast disabled
builtin_recastnavigation = "no"  # OK if navigation disabled

# Disabled modules for minimal build
module_godot_physics_2d_enabled = "no"
module_godot_physics_3d_enabled = "no"
module_jolt_physics_enabled = "no"
module_interactive_music_enabled = "no"
module_webp_enabled = "no"
module_glslang_enabled = "no"
module_basis_universal_enabled = "no"
module_bmp_enabled = "no"
module_camera_enabled = "no"
module_csg_enabled = "no"
module_dds_enabled = "no"
module_enet_enabled = "no"
module_freetype_enabled = "no"
module_gdscript_enabled = "no"
module_gltf_enabled = "no"
module_fbx_enabled = "no"
module_gridmap_enabled = "no"
module_hdr_enabled = "no"
module_jsonrpc_enabled = "no"
module_ktx_enabled = "no"
module_mbedtls_enabled = "no"
module_meshoptimizer_enabled = "no"
module_minimp3_enabled = "no"
module_mobile_vr_enabled = "no"
module_msdfgen_enabled = "no"
module_multiplayer_enabled = "no"
module_navigation_enabled = "no"
module_noise_enabled = "no"
module_ogg_enabled = "no"
module_openxr_enabled = "no"
module_raycast_enabled = "no"
module_regex_enabled = "no"
module_squish_enabled = "no"
module_svg_enabled = "no"
module_text_server_adv_enabled = "no"
module_tga_enabled = "no"
module_theora_enabled = "no"
module_upnp_enabled = "no"
module_vhacd_enabled = "no"
module_vorbis_enabled = "no"
module_webrtc_enabled = "no"
module_websocket_enabled = "no"
module_webxr_enabled = "no"
