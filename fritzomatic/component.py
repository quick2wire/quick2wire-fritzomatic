from fritzomatic.format import to_json, to_urltoken
from StringIO import StringIO
from zipfile import ZipFile, ZIP_DEFLATED

class Component(object):

  def title(self):
    return self.data.get('title', '')

  def label(self):
    return self.data.get('label', '')

  def description(self):
    return self.data.get('description', '')

  def tags(self):
    return self.data.get('tags', [])

  def connectors(self):
    return self.data.get('connectors', {})

  def json(self):
    return to_json(self.data)

  def urltoken(self):
    return to_urltoken(self.data)

  def module_id(self):
    return 'fedcf3d723271139dab3cc83d369dc6d' # TODO

  def fzpz(self):
    """Convert component to complete Fritzing .fzpz archive,
    which is basically a zip file containing the metadata
    and SVGs. Returns string of bytes"""
    data = StringIO()
    with ZipFile(data, compression=ZIP_DEFLATED, mode='w') as zf:
      zf.writestr('part.%s.fzp'           % self.module_id(), str(self.metadata()))
      zf.writestr('svg.icon.%s.svg'       % self.module_id(), str(self.icon()))
      zf.writestr('svg.breadboard.%s.svg' % self.module_id(), str(self.breadboard()))
      zf.writestr('svg.schematic.%s.svg'  % self.module_id(), str(self.schematic()))
      zf.writestr('svg.pch.%s.svg'        % self.module_id(), str(self.pcb()))
    data.seek(0)
    return data.getvalue()
