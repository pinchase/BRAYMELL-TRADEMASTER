#!/usr/bin/env python
import os
import sys
import traceback

if __name__ == '__main__':
    print(f"🔍 DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE')}", file=sys.stderr)
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        print(f"❌ Django import failed: {exc}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
    
    # Try to import settings explicitly
    try:
        from django.conf import settings
        print(f"✅ Settings loaded. INSTALLED_APPS: {settings.INSTALLED_APPS}", file=sys.stderr)
    except Exception as e:
        print(f"❌ Settings import failed: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
    
    execute_from_command_line(sys.argv)