local pwd = fs.getscriptdir(debug.getinfo(1).source)
local file = io.open(pwd..'input.txt')

local layersinfo,scanners_init,maxlayer = {},{},0
for line in file:lines() do
	local layer = line:cut('[: ]+')
	layersinfo[tonumber(layer[1])] = tonumber(layer[2])
	scanners_init[tonumber(layer[1])] = 1
	maxlayer = tonumber(layer[1])
end

local function calculate_severity(scanners,inittime)
	local severity,caught = 0,false
	for i = 0,maxlayer do
		if layersinfo[i] then
			local a = (layersinfo[i]-1)*(math.floor((i+inittime)/(layersinfo[i]-1))%2) -- Alternates 0 and 4
			local b = -(2*(math.floor((i+inittime)/(layersinfo[i]-1))%2)-1) -- Alternates 1 and -1
			local c = ((i+inittime)%(layersinfo[i]-1)) -- Modulo: goes 0,1,2,0,1,2,0,1,2...
			scanners[i] = a+b*c+1 -- Goes 1,2,3,4,3,2,1,2,3,4,3,2,1...
		end
		if scanners[i] == 1 then
			caught = true
			severity = severity+i*layersinfo[i]
		end
	end
	return severity,caught
end

local part1 = calculate_severity(scanners_init,0)

local part2,part2save,t1,t2 = 0,0,os.clock(),os.clock()-1
io.write('Calculating part 2: '..part2)
while select(2,calculate_severity(scanners_init,part2)) do
	if os.clock() >= t2+1 then
		backspace(string.len(part2save))
		io.write(part2)
		part2save = part2
		t2 = os.clock()
	end
	part2 = part2+1
end

print('\nPart 1: '..part1)
print('Part 2: '..part2)
print(string.format('Calculation time for part 2: %.1fs (%.1f iterations per second)',os.clock()-t1+0.5,part2/(os.clock()-t1+0.5)))