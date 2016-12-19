import sublime, sublime_plugin, datetime
class GitcommCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
		now = datetime.datetime.now()
		form = args['format']
		if form == 1:
			self.view.insert(edit, 0, now.strftime("%A %d %B %Y %H:%M:%S %p"))
		if form == 2:
			self.view.insert(edit, 0, now.strftime("%A %d %B %Y"))
		if form == 3:
			self.view.insert(edit, 0, now.strftime("%H:%M:%S %p"))
		if form == 4:
			self.view.insert(edit, 0, now.strftime("%Y-%m-%d %H:%M:%S"))
		if form == 5:
			self.view.insert(edit, 0, now.strftime("%a %d %b %Y %H:%M:%S"))
		if form == 6:
			self.view.insert(edit, 0, now.strftime("%Y/%m/%d"))
		if form == 7:
			self.view.insert(edit, 0, now.strftime("%d/%m/%Y"))
		if form == 8:
			self.view.insert(edit, 0, now.strftime("%B %d, %Y"))
		if form == 9:
			self.view.insert(edit, 0, now.strftime("%A %b %d"))		
		if form == 10:
			self.view.insert(edit, 0, now.strftime("%m/%d/%Y %H:%M:%S %p"))
