#!/usr/bin/env python

import datetime
import obspython as obs
import yaml

refresh_interval = 15000 # In milli seconds
file_path = ""

def script_description():
  return ('Conference programming read from a YAML file with schema:\n'
          '- current_title: "First Title"\n'
          '  current_presenter: "First Presenter"\n'
          '  next_title: "Next Title"\n'
          '  next_presenter: "Next Presenter"\n'
          '  next_time: 2018-07-01 10:00')

def script_properties():
  props = obs.obs_properties_create()
  obs.obs_properties_add_path(props, 'file_path', 'File Path', obs.OBS_PATH_FILE, 'YAML file (*.yml)', 'current.yml')
  return props

def script_update(settings):
  global refresh_interval
  global file_path

  obs.timer_remove(refresh_all)
  file_path = obs.obs_data_get_string(settings, "file_path")
  if file_path is not None:
    obs.timer_add(refresh_all, refresh_interval)

def refresh_all():
  global file_path
  
  if file_path is not None:
    with open(file_path, 'r') as current:
      try:
        session_yml = current.read()
        session = yaml.load(session_yml)[0]
        refresh_item('current_title', session['current_title'])
        refresh_item('current_presenter', session['current_presenter'])
        refresh_item('next_title', session['next_title'])
        refresh_item('next_presenter', session['next_presenter'])
        refresh_item('next_time', '{:%b %d %I:%M %p EST}'.format(datetime.datetime.strptime(session['next_time'], '%Y-%m-%d %H:%M')))
      except yaml.YAMLError as e:
        print(e)

def refresh_item(key, value):
  settings = obs.obs_data_create()
  obs.obs_data_set_string(settings, "text", value)  
  source = obs.obs_get_source_by_name(key)
  obs.obs_source_update(source, settings)
  obs.obs_data_release(settings)
  obs.obs_source_release(source)
  