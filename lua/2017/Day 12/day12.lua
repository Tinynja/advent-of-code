local pwd = fs.getscriptdir(debug.getinfo(1).source)
local file = io.open(pwd..'input.txt')

local network,remaining_ids = {},{}
for line in file:lines() do
	local inputs = line:cut('[ <>,-]+')
	remaining_ids[tonumber(inputs[1])] = tonumber(inputs[1])
	network[tonumber(inputs[1])] = {}
	for i = 2,#inputs do
		table.insert(network[tonumber(inputs[1])],tonumber(inputs[i]))
	end
end

file:close()

local function analyze_group(id,id_list)
	local id_list = id_list or {}
	id_list[id] = true
	for k,v in pairs(network[id]) do
		if not id_list[v] then
			id_list = analyze_group(v,id_list)
		end
	end
	return id_list
end

local part1ids,part1 = analyze_group(0),0
for k,v in pairs(part1ids) do
	part1 = part1+1
end

local part2,i = 0,next(remaining_ids)
repeat
	local group = analyze_group(i)
	for k,v in pairs(group) do
		remaining_ids[k] = nil
	end
	part2 = part2+1
	i = next(remaining_ids,i)
until i == nil

print('Part 1: '..part1)
print('Part 2: '..part2)