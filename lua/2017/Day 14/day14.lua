input = 'ljoxqyyw'

local function hex2bin(hex)
	hex = tonumber(hex,16)
	local bin = ''
	repeat
		bin = (hex%2)..bin
		hex = math.floor(hex/2)
	until hex == 0
	return bin
end

local function knot_hash(text)
end

for i = 0,127 do
	local hash = knot_hash(input..'-'..i)
	for j = 1,hash:len() do
		