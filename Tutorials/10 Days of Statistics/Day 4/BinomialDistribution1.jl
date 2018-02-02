function bin_dist(n, k, p, q)
    return binomial(n, k) * p^k * q^(n-k)
end

function f(p, q)
    p1 = bin_dist(6, 0, p, q)
    p2 = bin_dist(6, 1, p, q)
    p3 = bin_dist(6, 2, p, q)
    return 1 - p1 - p2 - p3
end

str = readline()
strvec = split(str, ' ')
floatvec = map(x -> parse(Float64, x), strvec)
a = floatvec[1]
b = floatvec[2]

p = a/(a+b)
q = b/(a+b)

print(round(f(p, q), 3))
