import numpy as np

class HMM():
	"""Class for Hidden Markov Model"""
	def __init__(self, labels, pi, transition, confusion):
		self.labels = labels
		self.pi = pi
		self.transition = transition
		self.confusion = confusion

	"""Evaluate the probability generated by this HMM given an observation sequence"""
	def evaluate(self, observation):
		partial = np.zeros([len(labels), len(observation)])
		for j in range(partial.shape[1]):
			for i in range(partial.shape[0]):
				if j == 0:
					partial[i, j] = pi[i] * confusion[i, observation[j]]
				else:
					partial[i, j] = sum(partial[: , j - 1] * transition[: , i]) * confusion[i, observation[j]]
		return sum(partial[:, -1])
 
 	"""Decode an observation sequence to a hidden state sequence"""
	def decode(self, observation):
		result = []
		partial = np.zeros([len(labels), len(observation)])
		for j in range(partial.shape[1]):
			maxIndex = 0
			for i in range(partial.shape[0]):
				if j == 0:
					partial[i, j] = pi[i] * confusion[i, observation[j]]
				else:
					partial[i, j] = max(partial[: , j - 1] * transition[: , i]) * confusion[i, observation[j]]
				if partial[i, j] > partial[maxIndex, j]:
					maxIndex = i
			result.append(maxIndex)
		return map(lambda item: labels[item], result)

	def learn(self):
		pass
		
labels = ['sunny', 'cloudy', 'rainy']
pi = np.array([0.63, 0.17, 0.2])
transition = np.array([
	[0.5, 0.375, 0.125],
	[0.25, 0.125, 0.625],
	[0.25, 0.375, 0.375]
])
confusion = np.array([
	[0.6, 0.2, 0.15, 0.05],
	[0.25, 0.25, 0.25, 0.25],
	[0.05, 0.1, 0.35, 0.5]
])

print(HMM(labels, pi, transition, confusion).evaluate([0,2,3]))
print(HMM(labels, pi, transition, confusion).decode([0,3,3,1,2]))