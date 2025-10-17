
import os
import sys
import shutil
import subprocess
import ninja.ninja

root_dir = os.path.abspath(os.path.dirname(__file__))
source_dir = f"{root_dir}/bzip2"
build_dir = f"{root_dir}/build"
install_dir = f"{root_dir}/install"
uv = shutil.which("uv")
cmake = shutil.which("cmake")

print(f"root directory - {root_dir}")
print(f"source directory - {source_dir}")
print(f"build directory - {build_dir}")
print(f"install directory - {install_dir}")
print(f"use cmake - {cmake}")
print(f"use uv - {uv}")

cmake = [cmake]

subprocess.run(cmake + ["-S", source_dir,
                        "-B", build_dir,
                        "-DCMAKE_BUILD_TYPE=Release",
                        f"-DCMAKE_INSTALL_PREFIX={install_dir}",
                        "-Wno-dev",
                        "-DENABLE_WERROR=OFF",
                        "-DENABLE_DEBUG=OFF",
                        "-DENABLE_APP=OFF",
                        "-DENABLE_DOCS=OFF",
                        "-DENABLE_EXAMPLES=OFF",
                        "-DENABLE_LIB_ONLY=ON",
                        "-DENABLE_STATIC_LIB=ON",
                        "-DENABLE_SHARED_LIB=ON"],
               cwd=source_dir,
               env=ninja.ninja.add_ninja(),
               check=True)

subprocess.run(cmake + ["--build", build_dir,"--config", "Release"],cwd=build_dir,env=ninja.ninja.add_ninja(),check=True)
subprocess.run(cmake + ["--install", build_dir,"--config", "Release"],cwd=build_dir,env=ninja.ninja.add_ninja(),check=True)
