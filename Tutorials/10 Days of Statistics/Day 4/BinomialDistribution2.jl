function bin_dist(n, k, p, q)
    return binomial(n, k) * p^k * q^(n-k)
end

function f(n, k, p, q)
    mass = 0
    for i = 0:k
        mass += bin_dist(n, i, p, q)
    end
    return mass
end

function g(n, k, p, q)
    mass = 0
    for i = k:n
        mass += bin_dist(n, i, p, q)
    end
    return mass
end

str = readline()
strvec = split(str, ' ')
intvec = map(x -> parse(Int64, x), strvec)
a = intvec[1]
n = intvec[2]

p = a / 100
q = 1 - p

println(round(f(n, 2, p, q), 3))
println(round(g(n, 2, p, q), 3))
