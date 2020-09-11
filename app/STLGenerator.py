import os

@staticmethod
def b(s, encoding='ascii', errors='replace'):  # pragma: no cover
    if isinstance(s, str):
        return bytes(s, encoding, errors)
    else:
        return s

class STLGenerator:
    @classmethod
    def save(self, filename, fh=None, mode='BINARY', update_normals=True):
        '''Save the STL to a (binary) file

        If mode is :py:data:`AUTOMATIC` an :py:data:`ASCII` file will be
        written if the output is a TTY and a :py:data:`BINARY` file otherwise.

        :param str filename: The file to load
        :param file fh: The file handle to open
        :param int mode: The mode to write, default is :py:data:`AUTOMATIC`.
        :param bool update_normals: Whether to update the normals
        '''
        assert filename, 'Filename is required for the STL headers'
        if update_normals:
            self.update_normals()

        if mode is 'BINARY':
            write = self._write_binary
        elif mode is 'ASCII':
            write = self._write_ascii
        else:
            raise ValueError('Mode %r is invalid' % mode)

        name = os.path.split(filename)[-1]
        try:
            if fh:
                write(fh, name)
            else:
                with open(filename, 'wb') as fh:
                    write(fh, filename)
        except IOError:  # pragma: no cover
            pass

    def _write_ascii(self, fh, name):
        if _speedups and self.speedups:  # pragma: no cover
            _speedups.ascii_write(fh, b(name), self.data)
        else:
            def p(s, file):
                file.write(b('%s\n' % s))

            p('solid %s' % name, file=fh)

            for row in self.data:
                vectors = row['vectors']
                p('facet normal %f %f %f' % tuple(row['normals']), file=fh)
                p('  outer loop', file=fh)
                p('    vertex %f %f %f' % tuple(vectors[0]), file=fh)
                p('    vertex %f %f %f' % tuple(vectors[1]), file=fh)
                p('    vertex %f %f %f' % tuple(vectors[2]), file=fh)
                p('  endloop', file=fh)
                p('endfacet', file=fh)

            p('endsolid %s' % name, file=fh)


