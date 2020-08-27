from src.entities.script import ScriptSchema
from src.repositories.script_repository import get_scripts, edit_script

def get_scripts_schema(session, scriptType, page, size):
  schema = ScriptSchema(many=True)
  page = get_scripts(session, scriptType, page, size)
  page.items = schema.dump(page.items)
  return page.__dict__

def edit_script_schema(script, session, status, report):
  schema = ScriptSchema(many=False)
  edited_script = edit_script(script, session, status, report)
  edited_script = schema.dump(edited_script)
  return edited_script.data