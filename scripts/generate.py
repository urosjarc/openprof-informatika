import importlib
import inspect
import json
import pkgutil
import types
import os
from dataclasses import dataclass, field, asdict

import requests

import naloge


@dataclass
class Naloga:
	ime: str
	docs: str
	resitve: dict = field(default_factory=dict)

	@staticmethod
	def src(ele):
		lines = inspect.getsource(ele)
		src = []
		start = 2
		for line in lines.split("\n"):
			if '"""' in line:
				start -= 1
				continue
			if start <= 0:
				src.append(line)
		return "\n".join(src)


@dataclass
class Module:
	ime: str
	common: str
	naloge: list[Naloga] = field(default_factory=list)

	@staticmethod
	def common(ele):
		lines = inspect.getsource(ele)
		src = []
		for line in lines.split("\n"):
			if line.startswith("def"):
				break
			src.append(line)
		return "\n".join(src)


@dataclass
class Package:
	modules: list[Module] = field(default_factory=list)


pkgpath = os.path.dirname(naloge.__file__)
paket = Package()
for module in pkgutil.iter_modules([pkgpath]):
	m = importlib.import_module(f"naloge.{module.name}")
	modul = Module(ime=module.name, common=Module.common(m))
	paket.modules.append(modul)

	for name, ele in m.__dict__.items():

		# NALOGE
		if isinstance(ele, types.FunctionType):
			naloga = Naloga(ime=name, docs=ele.__doc__)
			naloga.resitve['Python'] = Naloga.src(ele)
			modul.naloge.append(naloga)

with open("informatika.json", "w") as file:
	json.dump(asdict(paket), file, indent=4)
