class Automake (GnuPackage):
	def __init__ (self):
		GnuPackage.__init__ (self, 'automake', '1.13', override_properties = { 'build_dependency' : True })
		self.extra_stage_files = ['share/automake-%{version}/Automake/Config.pm']

	def deploy (self):
		# second build, to be bundled with the package
		self.package_prefix = self.profile.prefix
		self.staged_profile = self.profile.staged_prefix
		package_stage = self.do_build (self.profile.arch, self.workspace)
		merge_trees (package_stage, self.profile.staged_prefix)

	def arch_build (self, arch):
		if arch == 'darwin-universal':
			self.local_ld_flags = ['-arch i386' , '-arch x86_64']
			self.local_gcc_flags = ['-arch i386' , '-arch x86_64']
		elif arch == 'darwin-32':
			self.local_ld_flags = ['-arch i386','-m32']
			self.local_gcc_flags = ['-arch i386','-m32']
			self.local_configure_flags = ['--build=i386-apple-darwin11.2.0']
		elif arch == 'darwin-64':
			self.local_ld_flags = ['-arch x86_64 -m64']
			self.local_gcc_flags = ['-arch x86_64 -m64']
Automake()
