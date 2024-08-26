# Test using Shell script and G++.
g++ --version

# Build
LIBNAME="libsmath.so"
LIBDIR="libsmath/lib"
SRCDIR="libsmath/src"
SRC="$SRCDIR/smath.c"
TARGET="$LIBDIR/$LIBNAME"
OBJ="smath.o"

if [[ ! -f $TARGET ]]; then
  g++ -c -Wall -Werror -fpic $SRC &&
  g++ -shared -o $TARGET $OBJ &&
  rm $OBJ
fi

# C
EXE="c_test"
SRCTEST="test_c/test.c"
g++ -L"./$LIBDIR" -Wl,-rpath="./$LIBDIR" -Wall -o $EXE $SRCTEST -lsmath

if [[ -f $EXE ]]; then
  echo "$EXE executable file created ..."
else
  echo "$EXE executable file failed!"
  exit 0
fi

# Cpp
EXE="cpp_test"
SRCTEST="test_cpp/test.cpp"
g++ -std=c++2b -L"./$LIBDIR" -Wl,-rpath="./$LIBDIR" -Wall -o $EXE $SRCTEST -lsmath

if [[ -f $EXE ]]; then
  echo "$EXE executable file created ..."
else
  echo "$EXE executable file failed!"
  exit 0
fi


exit 0