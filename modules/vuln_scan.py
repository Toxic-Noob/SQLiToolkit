# Encoded By PyEncryptor
# A Product Of ToxicNoob
# https://github.com/Toxic-Noob

import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))