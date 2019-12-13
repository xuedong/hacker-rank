function neg_bin_dist(n, k, p, q)
    return binomial(n-1, k-1) * p^k * q^(n-k)
end

str = readline()
n = parse(Int64, readline())
strvec = split(str, ' ')
intvec = map(x -> parse(Int64, x), strvec)
a = intvec[1]
b = intvec[2]

p = a / b
q = 1 - p

println(round(neg_bin_dist(n, 1, p, q), 3))
