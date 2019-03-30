#生成指定分别的噪声
def get_delta(self, k, v):
    delta = math.gamma(k) / math.sqrt(math.gamma(k + 2 / v) * math.gamma(k) - math.gamma(k + 1 / v) ** 2)
    return delta

def get_pdf(self, x, delta, k, v):
    a = abs(v)
    b = delta * math.gamma(k)
    c = (x / delta) ** (k * v - 1)
    d = np.exp(-(x / delta) ** v)
    return a / b * c * d

def random_z(self, batch_size=16, z_dim=1, k=1.3, v=1.03):
    z = np.zeros(batch_size * z_dim)
    delta = self.get_delta(k, v)
    for i in range(batch_size * z_dim):
        while True:
            x = random.uniform(0.0, 4.0)                           
            y = random.uniform(0.0, 0.5)
            if y < self.get_pdf(x, delta, k, v):
                z[i] = x
                break
    z = z.reshape((batch_size, z_dim))
    if (len(z.shape) == 1):
        z = z[:, np.newaxis]
    return z
